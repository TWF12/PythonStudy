class User:
    def __init__(self, uid, pwd):
        self.uid = uid
        self.pwd = pwd

    def verify_pwd(self, input_pwd) -> bool:
        return self.pwd == input_pwd

    def has_perm(self, perm: str) -> bool:
        return False

""
class NUser(User):
    def __init__(self, uid, pwd, allowed_perms):
        super().__init__(uid, pwd)
        self.__allowed_perms = allowed_perms
    def has_perm(self, perm: str) -> bool:
        return True if perm in self.__allowed_perms else False

    def set_perm(self, perm):
            self.__allowed_perms.add(perm)


    def rm_perm(self, perm):
        if perm in self.__allowed_perms:
            self.__allowed_perms.remove(perm)

""
user1 = NUser("alice", 'pass123', {"read_file", "write_file"})
assert(
    issubclass(NUser, User) and hasattr(user1, '_NUser__allowed_perms')
    and not hasattr(user1, 'allowed_perms')
    and isinstance(user1._NUser__allowed_perms, set)
)

assert(user1.verify_pwd("pass123")) and not user1.verify_pwd("abc")
assert( not user1.has_perm("delete_user")) and user1.has_perm("read_file")

user1.set_perm("delete_file")
assert user1.has_perm("delete_file")

user1.rm_perm("delete_file")
assert not user1.has_perm("delete_file")

user1.rm_perm("read_user")
print("通过")