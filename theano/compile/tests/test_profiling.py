"""
Test of memory profiling

"""
import theano
import theano.tensor as T
import StringIO

def test_profiling():
	
	old1 = theano.config.profile 
	old2 = theano.config.profile_memory

	theano.config.profile = True
	theano.config.profile_memory = True
	
	x = T.dvector("x")
	y = T.dvector("y")
	z = x + y
	f = theano.function([x, y], z, profile=True, name="test_profiling")
	output = f([1, 2, 3, 4],[1, 1, 1, 1])

	buf = StringIO.StringIO()
	f.profile.summary(buf)
	
	theano.config.profile = old1
	theano.config.profile_memory = old2


if __name__ == '__main__':
	test_profiling()