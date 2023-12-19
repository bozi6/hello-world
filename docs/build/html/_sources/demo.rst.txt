Demo reStructuredText
*********************

.. meta::
   :keywords: backup
   :keywords lang=en: pleasefindthiskey pleasefindthiskeytoo
   :keywords lang=de: bittediesenkeyfinden

Lorem ipsum [Ref]_ dolor sit amet.
    .. [Ref] Book or article reference, URL or whatever.

Lorem ipsum [#f1]_ dolor sit amet ... [#f2]_

.. rubric:: Footnotes
.. [#f1] Text of the first footnote.
.. [#f2] Text of the second footnote.


.. code-block::
    :caption: A cool example
           The output of this line starts with four spaces.
.. code-block::

           The output of this line has no spaces at the beginning.

    def my_function(my_arg, my_other_arg):
        """A function just for me.

        :param my_arg: The first of my arguments.
        :param my_other_arg: The second of my arguments.

        :returns: A message (just for me, of course).

    """


:fieldname: Field content

This is a paragraph that contains `a link`_.

.. _a link: https://domain.invalid/

+------------------------+------------+----------+----------+
| Header row, column 1   | Header 2   | Header 3 | Header 4 |
| (header rows optional) |            |          |          |
+========================+============+==========+==========+
| body row 1, column 1   | column 2   | column 3 | column 4 |
+------------------------+------------+----------+----------+
| body row 2             | ...        | ...      |          |
+------------------------+------------+----------+----------+


>>> 1 + 1
    2

This is a normal text paragraph. The next paragraph is a code sample::

       It is not processed in any way, except
       that the indentation is removed.

       It can span multiple lines.

This is a normal text paragraph again.

one asterisk: *text* for emphasis (italics),
two asterisks: **text** for strong emphasis (boldface), and
backquotes: ``text`` for code samples.

* This is a bulleted list.
* It has two items, the second
  item uses two lines.

1. This is a numbered list.
2. It has two items too.

#. This is a numbered list.
#. It has two items too.

* this is
* a list

  * with a nested list
  * and some subitems

* and here the parent list continues

term (up to a line of text)
    Definition of the term, which must be indented

    and can even consist of multiple paragraphs

next term
Description.

    | These lines are
    | broken exactly like in
    | the source file.
