class StarCinema:
    hall_list = []

    def entry_hall(self, hall):
        self.hall_list.append(hall)


class Hall:
    def __init__(self, rows, cols, hall_no):
        self._seats = {}
        self._show_list = []
        self._rows = rows
        self._cols = cols
        self._hall_no = hall_no

    def get_show_list(self):
        return self._show_list

    def entry_show(self, show_id, movie_name, time):
        show_info = (show_id, movie_name, time)
        self._show_list.append(show_info)
        allocated_seats = [['free' for _ in range(self._cols)] for _ in range(self._rows)]
        self._seats[show_id] = allocated_seats

    def view_show_list(self):
        print("Now The Shows are running")
        for idx, show in enumerate(self._show_list):
            show_id, movie_name, show_time = show
            print(f"{idx}. Show ID: {show_id}, Movie: {movie_name}, Time: {show_time}")

    def book_seats(self, show_id, seats_to_book):
        if show_id not in self._seats:
            print("Invalid show ID")
            return

        for row, col in seats_to_book:
            if row < 1 or row > self._rows or col < 1 or col > self._cols:
                print(f"Invalid seat: {row}, {col}")
                continue

            if self._seats[show_id][row - 1][col - 1] != 'free':
                print(f"Seat {row}, {col} is already booked")
            else:
                self._seats[show_id][row - 1][col - 1] = 'booked'
                print(f"Seat {row}, {col} booked successfully")

    def view_available_seats(self, movie_id):
        if movie_id not in self._seats:
            print("Invalid show ID")
            return

        print(f"Available seats for show {movie_id}:")
        for i in range(self._rows):
            for j in range(self._cols):
                if self._seats[show_id][i][j] == 'free':
                    print(f"Row {i + 1}, Col {j + 1}")


def convert_to_tuples(numbers_str):
    numbers = list(map(int, numbers_str.split(', ')))
    tuples_list = [(numbers[i], numbers[i + 1]) for i in range(0, len(numbers), 2)]
    return tuples_list


oHall = Hall(5, 5, 2993)

oStarCinema = StarCinema()
oStarCinema.entry_hall(oHall)


oHall.entry_show(23234, "That's the life", "3: 30 pm")
oHall.entry_show(21234, "That's the boy", "4: 30 pm")


oHall.book_seats(23234, [(1, 2), (3, 4), (5, 5)])

while True:
    print("Welcome to our oStar Cinema")
    print("View All shows running right now, press: s")
    print("To View available seats, press: a")
    print("To book book a tickets, press: t")
    print("To quit, press: q")
    print()

    action = input("What do you want to do? ")
    action = action.lower()
    action = action[0]
    print()

    if action == 's':
        oHall.view_show_list()
    elif action == 'a':
        show_id = int(input("Pls, give me the show id. "))
        oHall.view_available_seats(show_id)
    elif action == 't':
        show_id = int(input("Pls, type the show id that you wanna watch. "))
        seats_num = input("give the seat numbers that you wanna book like comma separated number: 3, 4, 4, 5. ")
        seats_num = convert_to_tuples(seats_num)
        oHall.book_seats(show_id, seats_num)
    elif action == 'q':
        break
