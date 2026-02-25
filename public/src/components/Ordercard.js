export default function OrderCard({ order }) {

  if (!order) return null;

  return (
    <div className="order-card">

      <h3>{order.order_id}</h3>

      <p>Status: {order.status}</p>
      <p>City: {order.city}</p>
      <p>ETA: {order.eta}</p>
      <p>Refund: ₹{order.refund}</p>

    </div>
  );
}