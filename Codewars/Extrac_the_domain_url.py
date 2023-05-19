def domain_name(url):

        check = url[:3]

        if check == "htt":
            url = url.split('/')
            url.pop(0)
            url.pop(0)
            url = url[0]
            index2 = url.index('.')

            if url[:index2] == "www":
                url = url.split('.')
                url.pop(0)
                url.pop(1)
                return url[0]
            else:
                url = url[:index2]
                return url

        elif check == "www":
            url = url.split('.')
            url.pop(0)
            url.pop(1)
            return url[0]
        else:
            url = url.split('.')
            url.pop(1)
            return url[0]


# https://www.codewars.com/kata/514a024011ea4fb54200004b/train/python

if __name__ == "__main__":

    url = ('icann.org')
    
    print(domain_name(url))