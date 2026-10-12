from dataclasses import dataclass, field
from datetime import datetime, timezone

@dataclass
class Order:
    id: int
    user_id: int
    item_id: int
    quantity: int
    amount: int
    status: str
    payment_id: int | None = None
    idempotency_key: str | None = None
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

    def as_json(self) -> dict:
        return {
            "id": self.id,
            "userId": self.user_id,
            "itemId": self.item_id,
            "quantity": self.quantity,
            "amount": self.amount,
            "status": self.status,
            "paymentId": self.payment_id,
            "createdAt": self.created_at.isoformat(),
        }
