#!/usr/bin/env python

import itertools
import copy

from predicate import Predicate

class Rule(object):
    def __init__(self, s ):
        head, body = s.split(":-")
        self.head_pred = Predicate(head)

        self.body_preds = []
        j = 0
        while True:
            #i = body.find(')', j)

            i = body.find(',',j)
            if '(' in body[j:i]:
                i = body.find(')',j) + 1

            t = Predicate(body[j:i])
            self.body_preds.append( t )

            j = body.find(',', i)
            if j == -1:
                break
            else:
                j += 1

    def body_len(self):
        return len(self.body_preds)
    def max_arity(self):
        return max( self.head_pred.arity(), max( [ x.arity() for x in self.body_preds ] ) )

    def isomorphic_to(self, r):
        if not self.head_pred.match(r.head_pred, dict(), dict()):
            return False

        a1 = sorted([ b.arity() for b in self.body_preds ])
        a2 = sorted([ b.arity() for b in r.body_preds ])
        if a1 != a2:
            return False

        # test all permutation in body
        N = len(self.body_preds)
        for its in  itertools.permutations( range(N) ):
            matched = True
            rmp = dict()
            vmp = dict()

            # propogate maps: rmp vmp 
            assert self.head_pred.match(r.head_pred, rmp, vmp)

            for i,j in enumerate(its):
                pa = self.body_preds[i]
                pb = r.body_preds[j]
                matched = pa.match(pb, rmp, vmp)

                if not matched:
                    break

            if matched:
                # print rmp
                # print vmp
                # self.show()
                # r.show()                
                return True

        return False

    def to_template(self):
        p_mp = dict()
        v_mp = dict()
        hd = self.head_pred.to_template(p_mp, v_mp)
        bs = [ b.to_template(p_mp, v_mp) for b in self.body_preds ]
        s = '%s :- %s' % (hd, ','.join(bs) )
        #s = '%s & %s \\\\' % (hd, ','.join(bs) )
        return s

    def format_template(self):
        p_mp = dict()
        v_mp = dict()
        hd = self.head_pred.to_template(p_mp, v_mp)
        bs = [ b.to_template(p_mp, v_mp) for b in self.body_preds ]

        # define inner function
        #trans = lambda s: s.replace('(',' ').replace(')', ' ').replace(',', ' ')
        def trans (s):
            L = s.find('(')
            R = s.rfind(')')
            vs = map(int, s[L+1:R].split(','))
            
            return '%s %d %s' % ( s[:L], len(vs), ' '.join([str(v) for v in vs]) )

        ts = [hd] + bs

        print len(bs)
        for t in ts:
            print trans (t)


    def show_verbose(self):
        print '*Rule:'
        print '** Head:'
        self.head_pred.show()
        print '** Body:'
        for b in self.body_preds:
            b.show()


    def show_in_table(self):
        #print self.to_template()
        s = self.head_pred.to_str(), ' & ', ', '.join( [b.to_str() for b in self.body_preds] ), '\\\\'
        return ' '.join(s)
        #print s


    def show_metagol(self):
        rels = '%s,%s' % (self.head_pred.name, ','.join( b.name for b in self.body_preds) )
        head = self.head_pred.to_metagol()
        body = ','.join( [b.to_metagol() for b in self.body_preds] )
        s = 'metarule([%s], (%s :-[%s])).' % (rels, head, body)
        
        return s

    def __repr__(self):
        return '%s :- %s'  % ( self.head_pred.to_str(),  ','.join( [b.to_str() for b in self.body_preds] ) )

    def show(self):
        print str(self)
