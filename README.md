# Link2Json

link2Json

## Example how to use

```python
import link2json

my_dict = {'a': 123, 'b': 234}
print(f"1. UI JSON link - {link2json.get_ui_link(my_dict)}")
print(f"2. JSON link - {link2json.get_link(my_dict)}")

```
Output

1. UI JSON link - [http://jsonblob.com/1007976900349673472](http://jsonblob.com/1007976900349673472)

2. JSON link - [http://jsonblob.com/api/jsonBlob/1007976900349673472](http://jsonblob.com/api/jsonBlob/1007976900349673472)
