from blog_app.blog.models import Article
from blog_app.blog.queries import ListArticlesQuery, GetArticleByIDQuery


def test_list_articles():
    """
    GIVEN 2 articles stored in the database
    WHEN the execute method is called
    THEN it should return 2 articles
    """
    Article(
        author="jane@doe.com",
        title="New Article",
        content="Super extra awesome article",
    ).save()
    Article(
        author="jane@doe.com", title="Another Article", content="Super awesome article"
    ).save()

    query = ListArticlesQuery()

    assert len(query.execute()) == 2


def test_get_article_by_id():
    """
    GIVEN ID of article stored in the database
    WHEN the execute method is called on GetArticleByIDQuery with an ID
    THEN it should return the article with the same ID
    """
    article = Article(
        author="jane@doe.com",
        title="New Article",
        content="Super extra awesome article",
    ).save()

    query = GetArticleByIDQuery(id=article.id)

    assert query.execute().id == article.id
