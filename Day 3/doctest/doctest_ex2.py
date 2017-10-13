
class MyClass:
        pass

def unpred(obj):
        '''Returns unpredictable results
        >>> unpred(MyClass())#doctest:+ELLIPSIS
        <skip_doc.MyClass instance at 0x...>
        '''
        return obj
