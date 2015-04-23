Foreign Key Testing
===================

The `Onespacemedia <http://onespacemedia.com/>`_ team were experiencing a strange error whenever they ran ``./manage.py migrate`` on a new installation of the company CMS, under specific conditions. This project is a reduction of the CMS and all components of the bug down to the very bare minimum required to invoke the error.

To see it in action install the requirements and run ``./bisect.sh``, you should recieve the following traceback::

    Running migrations:
      Rendering model states...Traceback (most recent call last):
      File "./manage.py", line 10, in <module>
        execute_from_command_line(sys.argv)
      File "/Users/danielsamuels/Workspace/fk-testing/.venv/lib/python2.7/site-packages/django/core/management/__init__.py", line 338, in execute_from_command_line
        utility.execute()
      File "/Users/danielsamuels/Workspace/fk-testing/.venv/lib/python2.7/site-packages/django/core/management/__init__.py", line 330, in execute
        self.fetch_command(subcommand).run_from_argv(self.argv)
      File "/Users/danielsamuels/Workspace/fk-testing/.venv/lib/python2.7/site-packages/django/core/management/base.py", line 390, in run_from_argv
        self.execute(*args, **cmd_options)
      File "/Users/danielsamuels/Workspace/fk-testing/.venv/lib/python2.7/site-packages/django/core/management/base.py", line 441, in execute
        output = self.handle(*args, **options)
      File "/Users/danielsamuels/Workspace/fk-testing/.venv/lib/python2.7/site-packages/django/core/management/commands/migrate.py", line 221, in handle
        executor.migrate(targets, plan, fake=fake, fake_initial=fake_initial)
      File "/Users/danielsamuels/Workspace/fk-testing/.venv/lib/python2.7/site-packages/django/db/migrations/executor.py", line 104, in migrate
        state = migration.mutate_state(state, preserve=do_run)
      File "/Users/danielsamuels/Workspace/fk-testing/.venv/lib/python2.7/site-packages/django/db/migrations/migration.py", line 83, in mutate_state
        operation.state_forwards(self.app_label, new_state)
      File "/Users/danielsamuels/Workspace/fk-testing/.venv/lib/python2.7/site-packages/django/db/migrations/operations/fields.py", line 51, in state_forwards
        state.reload_model(app_label, self.model_name_lower)
      File "/Users/danielsamuels/Workspace/fk-testing/.venv/lib/python2.7/site-packages/django/db/migrations/state.py", line 97, in reload_model
        related_models = get_related_models_recursive(old_model)
      File "/Users/danielsamuels/Workspace/fk-testing/.venv/lib/python2.7/site-packages/django/db/migrations/state.py", line 57, in get_related_models_recursive
        rel_app_label, rel_model_name = rel_mod._meta.app_label, rel_mod._meta.model_name
    AttributeError: 'NoneType' object has no attribute '_meta'

Then head over to ``cms/apps/media/models.py`` and uncomment line 15, re-run ``./bisect.sh`` and you will see it works. Strange! If you comment out almost any field in the other models, you will see that it runs correctly.

When debugging the issue, it seems to be a reverse relation from Reversion - the ``Version.object`` field - which returns as 'None' for some reason.  Various things 'fixed' the error, including commenting out the 'Revision.user' field but these were not viable long-term fixes.  Simply changing the ForeignKey ``to`` value to a string rather than a direct model reference fixed the issue too, so that was the solution we ended up using.  There's likely some weird stuff happening with contenttypes or similar with regards to how they load models, that would likely be a good place to start if you're looking to debug the problem.

It's worth noting the specific commit in Django which caused this error to start occuring, it's `this one <https://github.com/django/django/commit/a1ba4627931591b80afa46e38e261f354151d91a>`_ as determined by a ``git bisect``.
