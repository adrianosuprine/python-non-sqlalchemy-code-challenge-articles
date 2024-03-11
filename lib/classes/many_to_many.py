class Article:
    # class attribute that stores all magazines
    all = []
    
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self._title = str(title)
        # appends data to the empty list
        Article.all.append(self)
        
    @property
    def title(self):
        return self._title
    @title.setter
    def title(self,new_title):
        return new_title
        
        
class Author:
    def __init__(self, name):
        self._name = name
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,new_name):
        self.new_name = new_name
        return self._name

    def articles(self):
        return [articles for articles in Article.all if articles.author == self]

    def magazines(self):
        return list(set([article.magazine for article in self.articles()]))

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        return article

    def topic_areas(self):
        return list(set([article.magazine.category for article in self.articles()])) if self.articles() else None

    def contributing_authors(self):
        return [author for author in Author.all if len(author.articles()) > 0]
class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def articles(self):
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass

# 