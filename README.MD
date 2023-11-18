**Enunciado del Problema: Sistema de Gestión de Biblioteca**

Has sido contratado para desarrollar un sistema de gestión de biblioteca que permita a los usuarios realizar préstamos y devoluciones de libros y revistas. El sistema debe incluir las siguientes clases:

### Clase `LibraryItem` (Clase Abstracta)

- Atributos:

  - `_title` (str): título del ítem de la biblioteca.
  - `_publication_year` (int): año de publicación del ítem.
  - `_is_available` (bool): indica si el ítem está disponible para préstamo.

- Métodos:
  - `__str__`: método abstracto para representar el ítem como una cadena.
  - `title` (property): propiedad para acceder al título.
  - `title` (setter): setter para modificar el título.
  - `is_available` (property): propiedad para verificar la disponibilidad.
  - `is_available` (setter): setter para actualizar la disponibilidad.

### Clase `Book` (Subclase de `LibraryItem`)

- Atributos Adicionales:

  - `_author` (str): autor del libro.
  - `_genre` (str): género del libro.

- Atributos de Clase:

  - `total_books` (int): total de libros en la biblioteca.
  - `books` (lista): lista de instancias de libros en la biblioteca.

- Métodos Adicionales:

  - `__str__`: método para representar el libro como una cadena.

- Métodos de Clase:
  - `find_book_by_title(cls, title)`: método de clase para buscar un libro por título.

### Clase `Magazine` (Subclase de `LibraryItem`)

- Atributos Adicionales:

  - `_editor` (str): editor de la revista.
  - `_is_borrowed` (bool): indica si la revista está prestada.

- Atributos de Clase:

  - `total_magazines` (int): total de revistas en la biblioteca.

- Métodos Adicionales:
  - `__str__`: método para representar la revista como una cadena.
  - `__lt__(self, other)`: método para comparar dos revistas por año de publicación.

### Clase `User`

- Atributos:

  - `_name` (str): nombre del usuario.
  - `_age` (int): edad del usuario.
  - `_id` (int): identificación única del usuario.
  - `_subscription_active` (bool): indica si la suscripción del usuario está activa.
  - `_borrowed_items` (lista): lista de ítems prestados por el usuario.

- Métodos:
  - `__str__`: método para representar al usuario como una cadena.
  - `deactivate_subscription`: desactiva la suscripción del usuario.
  - `activate_subscription`: activa la suscripción del usuario.
  - `add_item(item)`: agrega un ítem a la lista de ítems prestados por el usuario.
  - `remove_item(item)`: elimina un ítem de la lista de ítems prestados por el usuario.
  - `show_borrowed_items()`: muestra los ítems prestados por el usuario.

### Clase `Loan`

- Atributos:

  - `_library_item` (objeto `LibraryItem`): ítem prestado.
  - `_user` (objeto `User`): usuario que realiza el préstamo.
  - `_loan_date` (objeto `date`): fecha de préstamo.
  - `_return_date` (objeto `date`): fecha de devolución (puede ser `None` si el ítem aún no se ha devuelto).
  - `_is_active_loan` (bool): indica si el préstamo está activo.

- Métodos:
  - `calculate_loan_days()`: calcula la duración del préstamo en días.
  - `__str__`: método para representar el préstamo como una cadena.

### Clase `SubscriptionError` (Excepción)

- Atributo:

  - `message` (str): mensaje de error.

- Métodos:
  - `__init__`: inicializa la excepción.

### Clase `Library`

- Atributos:

  - `_books` (lista): lista de libros en la biblioteca.
  - `_magazines` (lista): lista de revistas en la biblioteca.
  - `_users` (lista): lista de usuarios registrados.
  - `_loans` (lista): lista de préstamos realizados.

- Métodos:
  - `add_library_item(library_item)`: agrega un ítem a la biblioteca.
  - `remove_library_item(library_item)`: elimina un ítem de la biblioteca.
  - `add_user(user)`: agrega un usuario a la biblioteca.
  - `remove_user(user)`:

elimina un usuario de la biblioteca.

- `show_library_items()`: muestra todos los ítems de la biblioteca.
- `show_users()`: muestra todos los usuarios registrados.
- `make_loan(loan)`: realiza un préstamo y lo agrega a la lista de préstamos.
- `search_library_items(title)`: busca un ítem en la biblioteca por título.

---

Con estas clases, podrás simular la gestión de préstamos y devoluciones en una biblioteca, manteniendo un seguimiento de los libros, revistas, usuarios y préstamos realizados.
