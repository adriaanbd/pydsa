class Group:
    def __init__(self, _name):
        self.name = _name
        self.groups = set()
        self.users = set()

    def add_group(self, group):
        self.groups.add(group)

    def add_user(self, user):
        self.users.add(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

    def __repr__(self):
        return f'{self.get_name()}'


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if user in group.get_users():
        return True

    groups = group.get_groups()

    if groups:
        for group in groups:
            return is_user_in_group(user, group)
    return False


if __name__ == '__main__':
    def test_subchild_user_is_found_in_parent():
        parent = Group("parent")
        child = Group("child")
        sub_child = Group("subchild")
        sub_child_user = "sub_child_user"
        sub_child.add_user(sub_child_user)
        child.add_group(sub_child)
        parent.add_group(child)

        return is_user_in_group(sub_child_user, parent)

    def test_child_user_is_found_in_parent():
        parent = Group("parent")
        child = Group("child")
        sub_child = Group("subchild")
        child_user = "child_user"
        child.add_user(child_user)
        child.add_group(sub_child)
        parent.add_group(child)

        return is_user_in_group(child_user, parent)

    def test_parent_user_not_found_in_child():
        parent = Group("parent")
        child = Group("child")
        sub_child = Group("subchild")
        parent_user = "parent_user"
        parent.add_user(parent_user)
        child.add_group(sub_child)
        parent.add_group(child)

        return is_user_in_group(parent_user, child)

    def test_different_inputs_child_user_found():
        parent = Group(10)
        child = Group(100)
        sub_child = Group(1000)
        child_user = None
        child.add_user(child_user)
        child.add_group(sub_child)
        parent.add_group(child)

        return is_user_in_group(child_user, parent)

    print(test_subchild_user_is_found_in_parent() is True)
    print(test_child_user_is_found_in_parent() is True)
    print(test_parent_user_not_found_in_child() is False)
    print(test_different_inputs_child_user_found() is True)
