
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._members = []


    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        member['id'] = self._generateId()
        self._members.append(member)
        return self._members

    def delete_member(self, id):
        for member in self._members:
            if member['id'] == id:
                self._members.remove(member)
                return self._members
        return None  # Return None if member with given id is not found

    def update_member(self, id, new_data):
        for member in self._members:
            if member['id'] == id:
                member.update(new_data)
                return self._members
        return None  # Return None if member with given id is not found

    def get_member(self, id):
        for member in self._members:
            if member['id'] == id:
                return member
        return None  # Return None if member with given id is not found

    def get_all_members(self):
        return self._members    


