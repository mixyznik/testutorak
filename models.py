class Comment(object):
    """Represent user."""

    def __init__(self, text, date):
        """Counstructor."""
        # super(User, self).__init__()
        self.text=text
        self.date=date
    def print_comments(self):
        print('Hello', self.text,self.date)

if __name__ == '__main__':
        COMMENTS = [
            Comment("hello", "2018-01-01"),
            Comment("world", "2018-01-02"),
            Comment("test", "2018-01-03"),
        ]

    # def __repr__(self):
    #     """Represent user as string."""
    #     return "text: {}, date: {}".format(
    #         self.text,
    #         self.date,
            
    #     )

#       def tr(self):
#         """Return user as HTML table row."""
#         tr = "<tr>"
#         tr += "<td>{}</td>".format(self.text)
#         tr += "<td>{}</td>".format(self.date)
#         tr += "</tr>"
#         return tr

# class UserManager(object):
#     """Manage users."""

#     def __init__(self, file):
#         """Constructor."""
#         self.file = file
#         self.users = []
#         with open(file) as f:
#             columns = None
#             for l in f.readlines():
#                 if not columns:
#                     columns = l.split(',')
#                     continue
#                 values = l.split(',')
#                 text = values[0]
#                 date = values[1]
#                 u = User(text, date)
#                 self.users.append(u)
#         self.columns = columns

#     def table(self):
#         """Retur users as HTML table."""
#         table_str = "<table>"

#         headers = '<tr>'
#         for column in self.columns:
#             th = "<th>{}</th>".format(column)
#             headers += th
#         headers += "</tr>"
#         table_str += headers

#         for user in self.users:
#             tr = user.tr()
#             table_str += tr

#         table_str += "</table>"
#         return table_str