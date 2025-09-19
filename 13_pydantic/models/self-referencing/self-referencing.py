# Now here it comes the time when we have to use something like a self referencing model.
# for example like a comment model can have a comment which can contain actual comment, then a reply to the comment which too will be of the same structure as of the comment.
# like an id, actual comment.


from __future__ import annotations
from pydantic import BaseModel, ValidationError
from typing import List, Optional

class Comment(BaseModel):
    id:int
    content:str
    replies:Optional[List[Comment]] = None

Comment.model_rebuild()




try:
    comment = Comment(id=101,content="First comment",replies=[
        Comment(id=102,content="reply to the first comment"),
        Comment(id=103,content="reply 2",replies=[
            Comment(id=104, content= "reply to the nested comment")
        ])
        ])
    print(comment)
except ValidationError as e:
    print(str(e))
