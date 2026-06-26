# Domain Model

```text
                Healthcare Management System

                           │
      ┌────────────┬─────────────┬─────────────┐
      │            │             │
   Patient      Doctor     Appointment
      │            │             │
      ├────────────┴─────────────┤
      │
Medical Record
      │
Prescription
```

## Core Entities

- Patient
- Doctor
- Appointment
- Medical Record
- Prescription

## Relationships

- A Patient can have many Appointments.
- A Doctor can have many Appointments.
- A Doctor writes many Prescriptions.
- A Patient has one Medical Record.