# class parent:
#   def properties(self) -> object:
#         self.props={"mobile":"oneplus","car":"swift"}
#         return self.props
# class child(parent):
#   def properties(self):
#     props=super().properties()
#     props["bike"]="duke"
#     return props
#
#
# c1=child()
# print(c1.properties())

class Editor:
    def functionalities(self):
        self.funcs=["createnewfiles","execute","save"]
        return self.funcs
class pycharm(Editor):
    def functionalities(self):
    funcs=super().functionalities()
    funcs.append("debug","versioncontrolling")
        return funcs
pyc=pycharm()
print(pyc.functionalities())
