import order
import receipt

# Opening
order.opening()

# Asking user to order ticket
ticketType_bool = order.asking()

# Choosing Ticket Type
ticketClass_bool = order.ticketType(ticketType_bool)
    
# Choosing Ticket Class
departure_bool = order.ticketClass(ticketClass_bool)
    
# Choosing Departure
data = order.data
destination_bool = order.departure(departure_bool,data)
    
# Choosing Destination

time_bool = order.destination(destination_bool,data)
    
# Choosing Departure Time
seat_bool = order.time(time_bool)

# Choosing Seat
price_bool = order.seat(seat_bool)

# Calculating Total Price
price = order.price(price_bool)

# Receipt
if price_bool:
    receipt.receipt(data,price)
    order.correct()