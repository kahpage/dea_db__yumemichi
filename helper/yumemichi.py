# Notes:
import sys
import json
from pathlib import Path
from typing import Any

# Add project root to sys.path (find the directory containing db_structs.py)
_root = Path(__file__).resolve().parent
while _root.parent != _root:
    if (_root / "db_structs.py").exists():
        if str(_root) not in sys.path:
            sys.path.append(str(_root))
        break
    _root = _root.parent

from db_structs import (
    Medium,
    Circle,
    Event,
    EventGroup,
    Source,
    ReliabilityTypes,
    OriginTypes,
    Location,
)

RT, OT = ReliabilityTypes, OriginTypes

PATH_HELPER = Path(__file__).parent
PATH_EVENT_GROUP = PATH_HELPER.parent
PATH_MEDIA = PATH_EVENT_GROUP / "media"


def retrieve_circles(event_name: str) -> list[Circle]:
    """Retrieve circles of given event. In the circle file has not been created, execute the creation script first."""
    circles_json_path = PATH_HELPER / event_name / "circles.json"
    if not circles_json_path.exists():
        print(
            f"Circle file for {event_name} not found, running the creation script ..."
        )
        creation_script_path = PATH_HELPER / event_name / "main.py"
        if not creation_script_path.exists():
            raise FileNotFoundError(
                f"Creation script for {event_name} not found at {creation_script_path}"
            )
        # Import main() from the creation script and execute
        import importlib.util

        spec = importlib.util.spec_from_file_location(
            f"{event_name}.main", creation_script_path
        )
        if spec and spec.loader:
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            if hasattr(module, "main"):
                module.main()

        if not circles_json_path.exists():
            raise FileNotFoundError(
                f"Creation script {creation_script_path} failed to create {circles_json_path}"
            )

    with circles_json_path.open("r", encoding="utf-8") as f:
        circles_raw = json.load(f)
    return [Circle.load_from_json(c) for c in circles_raw]


if __name__ == "__main__":
    events: list[Event] = []
    disabled_events: list[int | str] = []
    thwikicc = "https://thwiki.cc/%E6%A2%A6%E4%B9%8B%E4%B8%96%E7%BA%AA_%E9%AD%85%E7%9F%A5%E4%B9%8B%E6%97%85"

    i = 1  # ==== yumemichi1 ====
    if i not in disabled_events:
        event_name = f"yumemichi{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            Medium(
                "01_tirasi.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20180716092205id_/http://yumemichi.koromu-toho.com/",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
        ]
        locations = [
            Location(
                coordinates=(39.3282616, 141.5258479),
                address="1-10 Shinmachi, Tōno City, Iwate 028-0524, Japan",
                description="あえりあ遠野 2Fホール",
                sources=[
                    Source(
                        "https://web.archive.org/web/20180130193932id_/http://yumemichi.koromu-toho.com/gaiyou.php",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    ),
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-proxy/ALd4DhG8xbDYWhpELhBFht96ttxvhjpb5t6S2sdL-BP--cLQcv-oxPQ0KX3mKQ9S-ZSvL3v0O0CaKqByMwtpetOV9XdpaPlGIiQ7UqHS1glPIq3-lWErrplSnwmcM_oFn-etiqG8dZSVfNMgULyJxUiXEWnFTCBngcbB1gyXcQlOzIdld7TYefJNFodvTA=s0?imgmax=0",
                url="https://maps.app.goo.gl/HTd9UNmo2CHuKVcb9",
            ),
        ]
        event = Event(
            aliases=[
                "夢の世紀 魅知の旅",
                "Yume no Seiki Michi no Tabi",
                "yumemichi",
            ],
            dates="2014.03.02",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20180130193932/http://yumemichi.koromu-toho.com/gaiyou.php",
                    (RT.Reliable, OT.Official),
                ),
                Source(
                    "Participating circles: https://web.archive.org/web/20180716085719id_/http://yumemichi.koromu-toho.com/circle_list.php",
                    (RT.Reliable, OT.Official),
                ),
            ],
            locations=locations,
            description="Simultaneous with 東方紅楼夢9.5 遠野物語",
            # comments=None,
            last_edited="2026.10.17",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    i = 2  # ==== yumemichi2 ====
    if i not in disabled_events:
        event_name = f"yumemichi{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            Medium(
                "02_536px-东方红楼梦19.5梦之世纪_魅知之旅2插画2.jpg",
                [
                    Source(
                        "https://thwiki.cc/%E6%A2%A6%E4%B9%8B%E4%B8%96%E7%BA%AA_%E9%AD%85%E7%9F%A5%E4%B9%8B%E6%97%85",
                        (RT.Likely, OT.External),
                    )
                ],
            ),
            Medium(
                "02_-.webp",
                [
                    Source(
                        "https://web.archive.org/web/20240602210540/https://yumemichi.koromu-toho.com/",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            Medium(
                "02_image-1.webp",
                [
                    Source(
                        "https://web.archive.org/web/20240602210540/https://yumemichi.koromu-toho.com/",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            Medium(
                "02_touno.avif",
                [
                    Source(
                        "https://hamp.ai/event/yumemichi2024",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            Medium(
                "02_map_with_circles.svg",
                [
                    Source(
                        "https://hamp.ai/event/yumemichi2024",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            Medium(
                "02_东方红楼梦19.5梦之世纪_魅知之旅2插画1.jpg",
                [
                    Source(
                        "https://thwiki.cc/%E6%A2%A6%E4%B9%8B%E4%B8%96%E7%BA%AA_%E9%AD%85%E7%9F%A5%E4%B9%8B%E6%97%85",
                        (RT.Likely, OT.External),
                    )
                ],
            ),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
        ]
        locations = [
            Location(
                coordinates=(39.3282616, 141.5258479),
                address="1-10 Shinmachi, Tōno City, Iwate 028-0524, Japan",
                description="岩手県遠野市　あえりあ遠野",
                sources=[
                    Source(
                        "https://web.archive.org/web/20240422210747/https://koromu-toho.com/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    ),
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-proxy/ALd4DhG8xbDYWhpELhBFht96ttxvhjpb5t6S2sdL-BP--cLQcv-oxPQ0KX3mKQ9S-ZSvL3v0O0CaKqByMwtpetOV9XdpaPlGIiQ7UqHS1glPIq3-lWErrplSnwmcM_oFn-etiqG8dZSVfNMgULyJxUiXEWnFTCBngcbB1gyXcQlOzIdld7TYefJNFodvTA=s0?imgmax=0",
                url="https://maps.app.goo.gl/HTd9UNmo2CHuKVcb9",
            ),
        ]
        event = Event(
            aliases=[
                "夢の世紀 魅知の旅 再訪",
                "Yume no Seiki Michi no Tabi Saihou",
                "yumemichi 2",
            ],
            dates="2024.06.01",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20240422210747/https://koromu-toho.com/",
                    (RT.Reliable, OT.Official),
                ),
                Source(
                    "Participating circles: https://hamp.ai/event/yumemichi2024",
                    (RT.Reliable, OT.OfficialExt),
                ),
                Source(
                    "Participating circles (alt): https://web.archive.org/web/20250615161304/https://yumemichi.koromu-toho.com/koromu19-5_list/list_all.html",
                    (RT.Reliable, OT.Official),
                ),
            ],
            locations=locations,
            description="Simultaneous with 東方紅楼夢19.5 遠野物語",
            # comments=None,
            last_edited="2026.10.17",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    # i =   # ==== yumemichi ====
    # if i not in disabled_events:
    #     event_name = f"yumemichi{i}"
    #     print(f"Processing {event_name} ...")

    #     media_ = [
    #         # Medium("", [Source("", (RT.Reliable, OT.Official))]),
    #         # Medium("", [Source("", (RT.Reliable, OT.Official))]),
    #         # Medium("", [Source("", (RT.Reliable, OT.Official))]),
    #     ]
    #     locations = [
    #         # Location(
    #         #     coordinates=(,),
    #         #     address="",
    #         #     description="",
    #         #     sources=[Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))],
    #         #     # comments=None,
    #         #     imageUrl="",
    #         #     url="",
    #         # ),
    #     ]
    #     event = Event(
    #         aliases=,
    #         dates="",
    #         circles=[],
    #         media=media_,
    #         sources=[
    #             # Source("Date: ", (RT.Reliable, OT.Official)),
    #             # Source("Participating circles: ", (RT.Reliable, OT.Official)),
    #         ],
    #         locations=locations,
    #         description=None,
    #         # comments=None,
    #         # last_edited="",
    #     )

    #     # Retrieve circles
    #     # event.circles = retrieve_circles(event_name)
    #     events.append(event)

    # ==== event group ====
    media = [
        # Medium("",
        #        [Source("", (RT.Reliable, OT.Official))]),
        # Medium("",
        #        [Source("", (RT.Reliable, OT.Official))]),
    ]
    links = [
        "https://yumemichi.koromu-toho.com/",
    ]

    event_group = EventGroup(
        aliases=[
            "夢の世紀 魅知の旅",
            "Yume no Seiki Michi no Tabi",
            "yumemichi",
        ],
        events=events,
        media=media,
        links=links,
        sources=[
            Source(
                'Alias "yumemichi": url of main page at http://yumemichi.koromu-toho.com/',
                (RT.Reliable, OT.Official),
            ),
        ],
        comments=None,
        description="Companion to .5 events of 東方紅楼夢, themed around 秘封俱楽部.",
        last_edited="2026.10.17",
    )

    print(f"Saving {Path(__file__).stem} database...")
    event_group.save(PATH_EVENT_GROUP, indent=None)
    print("Done")
