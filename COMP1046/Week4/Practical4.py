class AcademicPublication:
    def __init__(self, year, title, authors=None):
        self.__year = year
        self.__title = title
        self.__authors = [] 

    def addAuthor(self, author):
        self.__authors.append(author)

    def getReference(self):
        author_str = ', '.join(self.__authors)
        reference_str = f"Authors: {author_str}\nPublication Details: ({self.__year}) {self.__title}"
        return reference_str

# Example usage
#publication = AcademicPublication(2023, "Father of The Atomic Bomb")
#publication.addAuthor("Robert Oppenheimer")
#publication.addAuthor("Christopher Nolan")
#print(publication.getReference())

class JournalArticle(AcademicPublication):
    def __init__(self, journalName, title, year, authors=None):
        super().__init__(year, title, authors)
        self.__journalName = journalName

    def getReference(self):
        parent_reference = super().getReference()
        reference_str = f"{parent_reference}.\nIn Journal of {self.__journalName}."
        return reference_str

# Example usage
#article = JournalArticle("ACM Computing Survey", "Information retrieval on the web", 2000)
#article.addAuthor("M Kobayashi")
#article.addAuthor("K Takeda")
#print(article.getReference())

class ConferencePaper(AcademicPublication):
    def __init__(self, year, title, authors=None):
        super().__init__(year, title, authors)
        self.conference = None

    def getReference(self):
        parent_reference = super().getReference()
        if self.conference is not None:
            reference_str = f"{parent_reference}.\nIn Proceedings of {self.conference.name} {self.conference.acronym}."
        else:
            reference_str = parent_reference
        return reference_str

# Example usage
#paper = ConferencePaper(2023, "Advances in AI", ["Alice", "Bob"])
#paper.setConference("International AI Conference", "IAC")
#print(paper.getReference())

class Conference:
    def __init__(self, acronym, name):
        self.acronym = acronym
        self.name = name
        self.papers = []

    def addPaper(self, paper):
        self.papers.append(paper)
        paper.conference = self

# Test cases
article1 = JournalArticle("ACM Computing Survey", "Information retrieval on the web", 2000)
article1.addAuthor("M Kobayashi")
article1.addAuthor("K Takeda")
print(article1.getReference())

paper1 = ConferencePaper(2021, "A Comparative Study of ML-ELM and DNN for Intrusion Detection")
paper1.addAuthor("Wencheng Yang")
paper1.addAuthor("Song Wang")
paper1.addAuthor("Michael N. Johnstone")

paper2 = ConferencePaper(2021, "A Survey on Formal Verification for Solidity Smart Contracts")
paper2.addAuthor("Ikram Garfatta")
paper2.addAuthor("Kais Klai")
paper2.addAuthor("Walid Gaaloul")
paper2.addAuthor("Mohamed Graiet")

acsw2021 = Conference("ACSW", "Australian Computer Science Week")
acsw2021.addPaper(paper1)
acsw2021.addPaper(paper2)

print(paper1.getReference())
print(paper2.getReference())

# Testing isinstance() and type()
print(isinstance(paper1, ConferencePaper))
print(isinstance(paper1, JournalArticle))
print(isinstance(acsw2021, Conference))
print(isinstance(article1, JournalArticle))
print(isinstance(article1, AcademicPublication))


print(type(paper2).__name__)
print(type(article1).__name__)
print(type(acsw2021).__name__)