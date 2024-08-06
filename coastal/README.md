# Coastal

Example `uwtools` invocation:

```
uw execute --module coastal.py --classname Coastal --task provisioned_rundir --config-file coastal.yaml --cycle 2024-08-05T12 --batch
```

Afterwards:

```
$ tree run
run
├── albedo.gr3 -> ../input/data/albedo.gr3
├── bctides.in -> ../input/data/bctides.in
├── datm_in
├── datm.streams
├── fd_ufs.yaml -> ../input/model/tests/parm/fd_ufs.yaml
├── hgrid.gr3 -> ../input/data/hgrid.gr3
├── hgrid.ll -> ../input/data/hgrid.ll
├── manning.gr3 -> ../input/data/manning.gr3
├── model_configure -> ../input/data/model_configure
├── noahmptable.tbl -> ../input/data/noahmptable.tbl
├── param.nml
├── runscript.coastal
├── station.in -> ../input/data/station.in
├── ufs.configure -> ../input/data/ufs.configure
├── vgrid.in -> ../input/data/vgrid.in
├── watertype.gr3 -> ../input/data/watertype.gr3
└── windrot_geo2proj.gr3 -> ../input/data/windrot_geo2proj.gr3

0 directories, 17 files
```
