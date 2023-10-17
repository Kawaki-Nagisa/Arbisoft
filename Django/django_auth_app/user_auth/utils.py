#utility functions for the user auth app

def chk_basic_auth(header):
    auth = header.split()
    if len(auth) == 2 and auth[0].lower() == "basic":
        email, password = (
                auth[1].encode("utf-8").decode("base64").split(":")
                    )
        return email, password
    else:
        return False
    