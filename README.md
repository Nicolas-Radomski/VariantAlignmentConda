# Usage
The main Python script VariantAlignment.py aims at performing variant compilation of bacterial genomes from a Python module genomic.py and a Conda environment PairedEndVariantCalling.
- This workflow run the consolidation of g.vcf.gz files (CombineGVCFs) from PairedEndVariant.py, joint-calling (GenotypeGVCFs), hard filtering of SNPs and InDels (SelectVariants and VariantFiltration) and merging of SNPs and InDels (MergeVcfs) based on GATK4 for downstream phylogenomic analyses.
- The main script VariantAlignment.py and module genomic.py (version 20201006, October 2020) were prepared and tested with Python and dependencies below.
- The module genomic.py has to be with the present main script VariantAlignment.py to lunch it properly.
- The Conda environment PairedEndVariantCalling has to be prepared as presented below.
- The user can setup his own dependencies in his own bin.
- The input g.vcf.gz files and indexed reference must be preferably prepared with PairedEndVariant.py.
- The user can use as input his own g.vcf.gz files and indexed reference.
# Dependencies
The main script VariantAlignment.py and module genomic.py (version 20201006) were prepared and tested with Conda packages below (Name/Version/Build/Channel).
- python/3.8.5/h1103e12_9_cpython/conda-forge
- biopython/1.78/py38h1e0a361_0/conda-forge
- gatk4/4.1.8.1/py38_0/bioconda
 Building of the Conda Environment PairedEndVariantCalling
## 1/ From available targeted Conda packages
```
conda activate
conda create -n PairedEndVariantCalling
conda activate PairedEndVariantCalling
conda search python
conda install -c conda-forge python=3.8.5=h1103e12_9_cpython
conda search biopython
conda install -c conda-forge biopython=1.78=py38h1e0a361_0
conda search gatk4
conda install -c bioconda gatk4=4.1.8.1=py38_0
```
## 2/ From available updated Conda packages
```
conda activate
conda create -n PairedEndVariantCalling
conda activate PairedEndVariantCalling
conda install -c conda-forge python
conda update -c conda-forge python
conda install -c conda-forge biopython
conda update -c conda-forge biopython
conda install -c bioconda gatk4
conda update -c bioconda gatk4
```
# Lunching of the script PairedEndVariantConda.py
## 1/ prepare a single command in a Bash script (bash_VariantAssemblyConda.sh)
```
#!/bin/bash
#SBATCH -p Research
#SBATCH -o %x.%N.%j.out
#SBATCH -e %x.%N.%j.err
#SBATCH --cpus-per-task=1
#SBATCH --job-name=test-20201006
source /global/conda/bin/activate;conda activate PairedEndVariantCalling; \
python /global/bio/projets/GAMeR/Nicolas-Radomski/PairedEndVariant/VariantAlignmentConda.py \
 -r VariantCalling \
 -gvcf /global/bio/projets/GAMeR/Nicolas-Radomski/PairedEndVariant/VariantCalling/5_calling \
 -ind /global/bio/projets/GAMeR/Nicolas-Radomski/PairedEndVariant/VariantCalling/1_reference/Enteritidis_P125109.fasta \
 -call /global/conda/envs/PairedEndVariantCalling/bin/gatk
```
## 2/ run the Bash script bash_VariantAssemblyConda.sh with sbatch
```
sbatch bash_VariantAssemblyConda.sh
```
# Check the numer of filtrated variants
## 1/ Single Nucleotide Polymorphisms (SNPs)
```
grep -v '#' /global/bio/projets/GAMeR/Nicolas-Radomski/PairedEndVariant/VariantCalling/7_alignment/filtered.snps.vcf | wc -l
```
## 2/ Small Insertions/Deletions (InDels)
```
grep -v '#' /global/bio/projets/GAMeR/Nicolas-Radomski/PairedEndVariant/VariantCalling/7_alignment/filtered.indels.vcf | wc -l
```
# Acknowledgment
My old colleagues Arnaud Felten and Ludovic Mallet with whom I learned a lot
# Author
Nicolas Radomski