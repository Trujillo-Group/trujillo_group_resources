# Loads g16 & executes GaussView
gaussview() {
    qrsh -l short
    module load apps/binapps/gaussian/g16c01_em64t
    gv &
}
