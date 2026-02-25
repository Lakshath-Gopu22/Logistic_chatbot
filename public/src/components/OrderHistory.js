export default function OrderHistory({ orders, onSelect }) {

  return (
    <div className="sidebar">

      <h3>Order History</h3>

      {orders.map((order) => (

        <div
          key={order.order_id}
          className="order-item"
          onClick={() => onSelect(order.order_id)}
        >
          {order.order_id}
        </div>

      ))}

    </div>
  );
}