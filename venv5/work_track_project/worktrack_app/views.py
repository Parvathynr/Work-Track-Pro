from http.client import HTTPResponse



# Create your views here.
def index(request):
    return HTTPResponse('hii how are u')

def sample(request):
    return HTTPResponse('test failed')

#push