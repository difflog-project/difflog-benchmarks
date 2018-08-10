
def get_pred_name(s):
    i = s.find('(')
    if i == -1:
        raise 'invalid format, cannot find pred_name in %s ' % s
    return s[:i]

def get_doms(s):
    L = s.find('(')
    R = s.rfind(')')
    if L == -1 or R == -1:
        raise 'invlaid format, cannot find doms in %s' % s

    vs = s[L+1:R].split(',')
    return [ v.strip() for v in vs ]


def encode(prefix, i):
    if Predicate.TemplateLevel == 0:
        return  '%s?' % prefix
    elif Predicate.TemplateLevel == 1:
        return  '%d' % i
    else:
        return  '%s%d' % (prefix, i)


ops = ['<=', '!=', '<', '=' ]
nms = ['LE', 'NE', 'LT', 'Eq']


class Predicate(object):
    TemplateLevel = 0
    def __init__(self, s):
        s2 = s.strip()
        if '<' in s or '=' in s:
            for i, op in enumerate(ops):
                if op in s:
                    self.name = nms[i]
                    self.doms = s.split(op)
                    break
        else:
            self.name = get_pred_name(s2)
            self.doms = get_doms(s2)

    def show(self):
        print 'Predicate: Name=%s, Doms=%s' % (self.name, self.doms)

    def to_str(self):
        return '%s(%s)' % (self.name, ','.join(self.doms))

    def to_metagol(self):
        return '[%s,%s]' % (self.name, (','.join(self.doms)).upper() )


    def arity(self):
        return len(self.doms)


    def match(self, pred, p_mp, v_mp):
        pa = self
        pb = pred

        if pa.arity() != pb.arity():
            return False

        # make pa_name is in different 'domain' from pb.name
        pa_name = '_' + pa.name

        if pa_name not in p_mp:
            # one-to-one mapping is required to guarantee isomorphic
            if pb.name in p_mp:
                return False
            p_mp[pa_name] = pb.name
            p_mp[pb.name] = pa_name
        elif p_mp[pa_name] != pb.name:
            return False


        for k in xrange( pa.arity() ):
            s = pa.doms[k]
            t = pb.doms[k]
            # make _s is in different domain from t
            _s = s * 1000
            if _s not in v_mp:
                # enforce one-to-one mapping
                if t in v_mp:
                    return False
                v_mp[ _s ] = t
                v_mp[ t ] = _s
            elif v_mp[ _s ] != t:
                return False

        return True


    def to_template(self, p_mp,  v_mp):
        if self.name not in p_mp:
            encode_name = encode('P', len(p_mp))
            # if Predicate.TemplateLevel > 0:
            #     encode_name = 'P%d' % len(p_mp)
            # else:
            #     encode_name = 'P?'
            p_mp[self.name] = encode_name
            
        for v in self.doms:
            if v not in v_mp:
                encode_name = encode('v', len(v_mp))
                # if Predicate.TemplateLevel > 0:
                #     encode_name = 'v%d' % len(v_mp)
                # else:
                #     encode_name = 'v?'
                v_mp[ v ] = encode_name


        s = '%s(%s)' % (p_mp[self.name], ','.join( [ v_mp[v] for v in self.doms ] ))
        return s
