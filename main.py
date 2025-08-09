import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)
    for user in data:
        Player.objects.create(
            nickname=user,
            email=data[user]["email"],
            bio=data[user]["bio"],
            race=Race.objects.get_or_create(
                name=data[user]["race"]["name"],
                description=data[user]["race"]["description"]
            )[0],

            guild=Guild.objects.get_or_create(
                name=data[user]["guild"]["name"],
                description=data[user]["guild"]["description"])[0]
            if data[user]["guild"] else None,
        )
        skills = data[user]["race"]["skills"]
        for skill in skills:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=Race.objects.get(name=data[user]["race"]["name"])
            )


if __name__ == "__main__":
    main()
