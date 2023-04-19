Create new todos
================


Instructions
------------

In the application directory, run the following command:

.. code-block:: console

    $ python manage.py shell_plus

Sample todos list
-----------------

.. code-block:: console

    User = get_user_model()

    Todo.objects.create(
        title = "Test Todo 1",
        body = "This is a test from the shell",
    )
    Todo.objects.create(
        title = "Learn Python",
        body = "",
    )
    Todo.objects.create(
        title = "Build a time machine",
        body = "",
    )
    Todo.objects.create(
        title = "Learn to play a song on guitar",
        body = "",
    )
    Todo.objects.create(
        title = "Improve cooking skills",
        body = "Use the recipe for the bolognese sauce",
    )
    Todo.objects.create(
        title = "Draw a picture",
        body = "Finish drawing of the fish",
    )
    Todo.objects.create(
        title = "Mend a shirt",
        body = "Find a new button for the blue dress shirt",
    )
    Todo.objects.create(
        title = "Change a car tire",
        body = "Don't forget to check the oil as well",
    )
    Todo.objects.create(
        title = "Write a letter",
        body = "Send a thank you note for birthday gift",
    )
    Todo.objects.create(
        title = "Plan an invasion",
        body = "",
    )
    Todo.objects.create(
        title = "Write a sonnet",
        body = "",
    )
    Todo.objects.create(
        title = "Balance accounts",
        body = "Find out about that missing shipment",
    )
    Todo.objects.create(
        title = "Program a computer",
        body = "",
    )
    Todo.objects.create(
        title = "Learn Django",
        body = "Make a cool web application",
    )
