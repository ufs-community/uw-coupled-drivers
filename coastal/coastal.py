"""
A driver for the Coastal App coupled executable.
"""

from iotaa import Asset, task, collection
from uwtools.api.cdeps import CDEPS
from uwtools.api.driver import DriverCycleBased
from uwtools.api.fs import link
from uwtools.api.logging import use_uwtools_logger
from uwtools.api.schism import SCHISM

use_uwtools_logger()


class Coastal(DriverCycleBased):
    """
    A driver for the Coastal App coupled executable.
    """

    @task
    def linked_files(self):
        """
        Data files linked into the run directory.
        """
        links = self.config["links"]
        path = lambda fn: self.rundir / fn
        yield self.taskname("Linked files")
        yield [Asset(path(fn), path(fn).is_file) for fn in links.keys()]
        yield None
        link(config=links, target_dir=self.rundir)

    @collection
    def provisioned_rundir(self):
        """
        The run directory provisioned with all required content.
        """
        cdeps = CDEPS(config=self.config_full, cycle=self.cycle, controller=[self.driver_name()])
        schism = SCHISM(config=self.config_full, cycle=self.cycle, controller=[self.driver_name()])
        yield self.taskname("Provisioned run directory")
        yield [
            cdeps.atm_nml(),
            cdeps.atm_stream(),
            schism.namelist_file(),
            self.linked_files(),
            self.restart_dir(),
            self.runscript(),
        ]

    @task
    def restart_dir(self):
        """
        RESTART directory in run directory.
        """
        path = self.rundir / "RESTART"
        yield self.taskname("RESTART directory")
        yield Asset(path, path.is_dir)
        yield None
        path.mkdir(parents=True)

    def driver_name(self):
        return "coastal"
