import logging
from kik_unofficial.client import KikClient
from kik_unofficial.callbacks import KikClientCallback
from typing import Union
from kik_unofficial.datatypes.xmpp.xiphias import UsersResponse, UsersByAliasResponse

HOST, PORT = "talk1110an.kik.com", 5223
log = logging.getLogger('kik_unofficial')

def resolve():
    def main():  # This function is used to execute the login process only if the file was run directly, and not imported.
        ResolveAjid()


    class ResolveAjid(KikClientCallback):
        def __init__(self):  # Constructor for the ResolveAjid class above
            self.client = KikClient(callback=self, kik_username=None, kik_password=None, device_id_override='IML74K',
                                    android_id_override='dfb2b4172c4eab65')
            print(("Retrieving ajids from ajids.txt"))
            with open('ajids.txt', "r") as f:
                ajid_list = f.read().splitlines()
                print((f"{len(ajid_list)} has been retrieved"))

            for ajid in ajid_list:
                print("ajid: ", ajid)
                print("request_info_of_users: ", self.client.request_info_of_users(ajid))
                print("xiphias_get_users: ", self.client.xiphias_get_users(ajid))
                print("xiphias_get_users_by_alias: ", self.client.xiphias_get_users_by_alias(ajid))
                print("\n")
            self.client.disconnect()



    if __name__ == '__main__':  # This is used to execute the login process only if the file was run directly, and not imported.
        # logging.basicConfig(format=RegisterClient.log_format(), level=logging.DEBUG)
        main()

resolve()
