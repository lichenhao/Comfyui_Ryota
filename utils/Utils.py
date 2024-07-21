import numpy as np
import torch
from PIL import Image

def ReverseTuples(tuples):
    new_tup = tuples[::-1]
    return new_tup

 
def Camelcase2Split(str):
    words = [[str[0]]]
 
    for c in str[1:]:
        if words[-1][-1].islower() and c.isupper():
            words.append(list(c))
        else:
            words[-1].append(c)
    return ' '.join([''.join(word) for word in words])

# Hack: string type that is always equal in not equal comparisons
class AnyType(str):
    def __ne__(self, __value: object) -> bool:
        return False
# Our any instance wants to be a wildcard string
any = AnyType("*")

def tensor2pil(image):
    return Image.fromarray(np.clip(255. * image.cpu().numpy().squeeze(), 0, 255).astype(np.uint8))


def pil2tensor(image):
    return torch.from_numpy(np.array(image).astype(np.float32) / 255.0).unsqueeze(0) 
