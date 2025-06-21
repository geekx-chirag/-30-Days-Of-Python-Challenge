from dataclasses import dataclass

@dataclass
class MarvelComic:
    title: str
    hero: str
    issue_number: int
    year: int

    def display_details(self):
        print("Marvel Comic Details:")
        print(f"Title: {self.title}")
        print(f"Hero: {self.hero}")
        print(f"Issue #: {self.issue_number}")
        print(f"Year: {self.year}")

# Example use
comic1 = MarvelComic(
    title="Doctor Strange: Multiverse Of Madness",
    hero="Doctor Strange",
    issue_number=1,
    year= 2023
)

comic1.display_details()
