
# from dataclasses import dataclass, field, asdict, astuple

# @dataclass(frozen=True, order=True)
# class Comment:
#     id: int = field(compare=False, hash=False, repr=False)
#     likes: str = field(default=0)
#     replies: list[int] = field(default_factory=[], compare=False, hash=False)
#     text: str = field(default="No comment.")

# # # Create a Comment object.
# comment_1 = Comment(id=2, likes=4, text="This is a comment.", replies=[])
# print(comment_1)
# comment_2 = Comment(1, "This is a comment.", 5, [2, 3, 4])

# Print the Comment object.
# comment.id = 1 # AttributeError: cannot assign to field 'id'
# print(comment_1 == comment_2) # [2, 3, 4]


# with dataclass decorator we don't need to define __init__ method anymore, it is done automatically
# Simple Class we write megic methods like __init__ and __repr__ manually but with dataclass decorator we don't need to do that


# __post_init__ method is called after __init__ method and it is used to do some post initialization work
# __setattr__ method is called when we try to set an attribute on an object
# __getattr__ method is called when we try to get an attribute on an object
# __delattr__ method is called when we try to delete an attribute on an object


from dataclasses import dataclass

@dataclass(order=True)
class PlayingCard:
    rank: str
    suit: str

    def __str__(self):
        return f'{self.suit}{self.rank}'
    

# Create a PlayingCard object.
card_1 = PlayingCard('A', '♠')
card_2 = PlayingCard('B', '♣')

# Print the PlayingCard object.
print(card_1)
print(card_2)
print(card_1 == card_2)
print(card_1 > card_2)
