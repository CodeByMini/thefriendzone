from engine.engine import Engine

if __name__ == '__main__':
   
    engine = Engine()
    engine.add_user("userOne", "devtest")
    
    while True:
        print("Welcome to the social media of the future.")
        
        print("Enter username to log in.")
        username = "userOne" #input("-> ")
        
        print("Enter password")
        password = "devtest" #input("-> ")
        
        try:
            user = engine.log_in(username, password)
        except RuntimeError:
            print("Wrong username or password, try again.")
            continue
        else:
            break

    print(f"Welcome, {user.username}")

    """
    TODO:

        * Write menu for what should happen when user signs in
        * Allow users to create posts, browse other users if they're friends with them
        * Correct the JSON serialization so that all properties are correctly saved // move to pickle
        * Store passwords hashed, not plain string. Who's responsible? User? Engine? DAO? 

    """