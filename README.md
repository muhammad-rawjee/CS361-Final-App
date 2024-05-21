# CS361-Final-App

## UML Sequence Diagram: 
![Sequence Diagram_ Phone Call](https://github.com/muhammad-rawjee/CS361-Final-App/assets/62274811/00d1b44d-b786-4533-82db-e22b4b714e09)

### 1. Requesting Data from TICTAK Service:

```To request data from the TICTAK service, you need to write the command 'run' to the tictak-service.txt file.```
#### Example

```
def request_board():
    with open('tictak-service.txt', 'w') as file:
        file.write('run')
    print("Requested TICTAK Service to generate a board.")
```
### 2. Receiving Data from Winner Service:
```To receive the winner from the Winner Service, you need to read the winner-service-output.txt file.```
#### Example
```
def receive_winner():
    while not os.path.exists('winner-service-output.txt') or os.path.getsize('winner-service-output.txt') == 0:
        time.sleep(1)
    with open('winner-service-output.txt', 'r') as file:
        winner = file.read().strip()
    print("Received winner from Winner Service.")
    return winner
```
