import random
import math

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        self.number_of_times_that_we_called_add_friend += 1
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        self.number_of_times_that_we_called_add_friend = 0
        # !!!! IMPLEMENT ME

        # Add users
        for i in range(num_users):
            self.add_user(f"Dude number {i + 1}")

        # Create all possible friendship combinations
        possible_friendships = []
        for userID in self.users:
            for friendID in range(userID + 1, self.last_id + 1):
                possible_friendships.append((userID, friendID))
        #shuffling
        random.shuffle(possible_friendships)
        #slicing
        friendships_to_add = possible_friendships[0:num_users * avg_friendships // 2]
        #adding in alla them friendships
        for friendship in friendships_to_add:
            self.add_friendship(friendship[0], friendship[1])

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        #queue for breadth first searching
        queue = []
        #breadth first searching
        queue.append([user_id])

        while len(queue) > 0:
            path = queue.pop(0)
            friend_id = path[-1]

            if friend_id not in visited:
                visited[friend_id] = path

                for next_friend_id in self.friendships[friend_id]:
                    new_path = path + [next_friend_id]
                    queue.append(new_path)
        #after it breadth first searches all of the paths it returns the list of all of the paths
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(100, 10)
    print(sg.number_of_times_that_we_called_add_friend)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
