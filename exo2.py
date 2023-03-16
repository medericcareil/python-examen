from data.user_infos import user_infos
from src.user import User

def main() -> None:
    u = User(
        user_infos['firstname'],
        user_infos['lastname'],
        user_infos['age'],
        user_infos['gender'],
        user_infos['job']
    )
    u.to_json()

if __name__ == '__main__':
    main()
