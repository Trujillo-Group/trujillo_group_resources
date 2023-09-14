# Gaussview function
gaussview() {
        # Store the current working directory
        cwd=$(pwd)

        # Run qrsh to start a remote shell
        qrsh -l short <<EOF

        # Load the required module
        module load apps/binapps/gaussian/g16c01_em64t
      
        # Run the gv command with the provided file name
        gv "$cwd/$1"
EOF
}
