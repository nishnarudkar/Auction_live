import streamlit as st

# Initialize session state for bids and auction reset
if "bids" not in st.session_state:
    st.session_state.bids = {}

if "auction_active" not in st.session_state:
    st.session_state.auction_active = True


# Function to find the highest bidder
def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    return winner, highest_bid


# Function to reset the auction
def reset_auction():
    st.session_state.bids = {}
    st.session_state.auction_active = True
    st.success("The auction has been reset!")


st.title("Auction App")

if st.session_state.auction_active:
    st.subheader("Place Your Bid")

    # Input fields for user name and bid
    name = st.text_input("Enter your name:")
    price = st.number_input("Enter your bid ($):", min_value=0, step=1)

    if st.button("Submit Bid"):
        if name and price > 0:
            st.session_state.bids[name] = price
            st.success(f"Bid placed successfully by {name} with ${price}!")
        else:
            st.error("Please provide a valid name and bid.")

    # Check if there are more bidders
    if st.button("End Auction"):
        st.session_state.auction_active = False

else:
    # Display the winner
    winner, highest_bid = find_highest_bidder(st.session_state.bids)
    if winner:
        st.subheader(f"The winner is {winner} with a bid of ${highest_bid}!")
    else:
        st.subheader("No bids were placed.")

    # Button to reset the auction
    if st.button("Reset Auction"):
        reset_auction()
