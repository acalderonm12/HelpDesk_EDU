import pytest
from app.services.tickets import TicketService
from app.models.entities import User, Ticket
from app.domain.erros import PermissionDeniedError, ValidationError

def test_add_internal_note_success():
  
    service = TicketService()
    
   
    staff_user = service._users.add(User(id=1, name="Ingeniero Soporte", email="staff@helpdesk.com", is_staff=True))
    client_user = service._users.add(User(id=2, name="Cliente Final", email="client@helpdesk.com", is_staff=False))
    
  
    ticket = service.create_ticket(requester_id=client_user.id, title="Falla en red", description="No hay internet")
    
   
    note = service.add_internal_note(
        ticket_id=ticket.id,
        author_id=staff_user.id,
        body="Revisar el switch principal del edificio."
    )
    
    assert note.id == 1
    assert note.ticket_id == ticket.id
    assert note.author_id == staff_user.id
    assert note.body == "Revisar el switch principal del edificio."
    assert len(ticket.internal_notes) == 1


def test_add_internal_note_permission_denied():
  
    service = TicketService()
    
    client_user = service._users.add(User(id=2, name="Cliente Final", email="client@helpdesk.com", is_staff=False))
    ticket = service.create_ticket(requester_id=client_user.id, title="Falla", description="Error")
    
    # Intentar agregar nota interna con un usuario que no es staff debe lanzar PermissionDeniedError
    with pytest.raises(PermissionDeniedError):
        service.add_internal_note(
            ticket_id=ticket.id,
            author_id=client_user.id,
            body="Nota maliciosa de cliente"
        )