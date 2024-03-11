class Article:
    # class attribute that stores all magazines
    all = []
    
    def __init__(self, author, magazine, title):
        self.author = author
        self._author = author
        self.magazine = magazine
        self._title = title
        # appends data to the empty list
        Article.all.append(self)
        
#         Article __init__(self, author, magazine, title)
# Article is initialized with an Author instance, a Magazine instance, and a title.
# Article property title
# Returns the article's title
# Titles must be of type str
# Titles must be between 5 and 50 characters, inclusive
# Should not be able to change after the article is instantiated.
# hint: hasattr()
        
    @property
    def title(self):
        return self._title
    @title.setter
    def title(self,title):
        if not isinstance (title, str) or 5 <= len(title) <= 50:
            raise ValueError('Invalid title')
        else:
            self._title = title
        
        
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
        self._name = name
        self._category = category
        
    @property
    def name(self):
        return self._name
    @property
    def category(self):
        return self._category
    @name.setter 
    def name(self,new_name):
        if isinstance (new_name,str):
            if len(new_name) >= 2 and len(new_name)  <= 16:
                self._name = new_name
        return self._name
    
    @category.setter 
    def category(self,new_category):
        if isinstance (new_category,str):
            if len(new_category) > 0:
                self._category = new_category
        return self._category
    

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list(set([article.author for article in self.articles()]))

    def article_titles(self):
        titles = [article.title for article in self.articles()]
        if titles:
            return titles 
        else:
            None
        

    def contributing_authors(self):
        authors = {}
        for article in self.articles():
            if article.author in authors:
                authors[article.author] += 1
            else:
                authors[article.author] = 1
        contributing_authors = [author for author, count in authors.items() if count > 2]
        if contributing_authors:
            return contributing_authors
        else:
            None






