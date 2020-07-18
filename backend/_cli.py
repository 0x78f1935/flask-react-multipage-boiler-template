from flask import current_app
import pathlib


def register(app):
    @app.cli.group()
    def unit():
        """
        Starts certain unittest, for a for list type \"dir\" ad argument
        """
        pass

    @unit.command()
    def test():
        """
        Start unittests
        """
        from backend.unittest import BoilerUnitTest
        BoilerUnitTest.run()
        print('success :D')

    @app.cli.group()
    def dev():
        """
        Debug tools
        """
        print("PLACEHOLDER")

    @dev.command()
    def clear():
        """
        Clears whole database, only in debug mode
        """
        from backend import db
        if current_app.config["TESTING"]:
            meta = db.metadata
            for table in reversed(meta.sorted_tables):
                print(f'Clear table {table}')
                db.session.execute(table.delete())
            db.session.commit()
        print("Done")