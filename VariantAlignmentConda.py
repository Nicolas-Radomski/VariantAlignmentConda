#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

#### author: Nicolas Radomski ####
# version for conda in a cluster: conda enviroment PairedEndVariantCalling
# run consolidation of g.vcf.gz files (CombineGVCFs) from PairedEndVariant.py, joint-calling (GenotypeGVCFs), hard filtering of SNPs and InDels (SelectVariants and VariantFiltration) and merging of SNPs and InDels (MergeVcfs) based on GATK4 for downstream phylogenomic analyses
# the module genomic.py has to be with the present main script PairedEndAssemblyConda.py to lunch it properly
# the present main script VariantAlignment.py and module genomic.py (version 20201006, Octobre 2020) were prepared and tested with Python and Conda packages below (Name/Version/Build/Channel)
#- python/3.8.5/h1103e12_9_cpython/conda-forge
#- biopython/1.78/py38h1e0a361_0/conda-forge
#- gatk4/4.1.8.1/py38_0/bioconda
# the present main script VariantAlignment.py executes more precisly the commands below
#### Execute ls /global/bio/projets/GAMeR/Nicolas-Radomski/PairedEndVariant/VariantCalling/5_calling/*.g.vcf.gz | tr 'n\' '%' | sed 's@.$@@' | sed 's@%@ -V @'g > /global/bio/projets/GAMeR/Nicolas-Radomski/PairedEndVariant/VariantCalling/7_alignment/gvcfpaths.txt
#### Execute /global/conda/envs/PairedEndVariantCalling/bin/gatk --java-options "-Xms50g -Xmx50g" CombineGVCFs -R /global/bio/projets/GAMeR/Nicolas-Radomski/PairedEndVariant/VariantCalling/1_reference/Enteritidis_P125109.fasta -V /global/bio/projets/GAMeR/Nicolas-Radomski/PairedEndVariant/VariantCalling/5_calling/ERR3997398.g.vcf.gz -V /global/bio/projets/GAMeR/Nicolas-Radomski/PairedEndVariant/VariantCalling/5_calling/ERR3997399.g.vcf.gz -V /global/bio/projets/GAMeR/Nicolas-Radomski/PairedEndVariant/VariantCalling/5_calling/ERR3997400.g.vcf.gz -V /global/bio/projets/GAMeR/Nicolas-Radomski/PairedEndVariant/VariantCalling/5_calling/ERR3997402.g.vcf.gz -V /global/bio/projets/GAMeR/Nicolas-Radomski/PairedEndVariant/VariantCalling/5_calling/ERR3997404.g.vcf.gz -V /global/bio/projets/GAMeR/Nicolas-Radomski/PairedEndVariant/VariantCalling/5_calling/ERR3997405.g.vcf.gz -V /global/bio/projets/GAMeR/Nicolas-Radomski/PairedEndVariant/VariantCalling/5_calling/ERR3997407.g.vcf.gz -V /global/bio/projets/GAMeR/Nicolas-Radomski/PairedEndVariant/VariantCalling/5_calling/ERR3997409.g.vcf.gz -O /global/bio/projets/GAMeR/Nicolas-Radomski/PairedEndVariant/VariantCalling/7_alignment/combined.g.vcf.gz -G AS_StandardAnnotation -G StandardHCAnnotation
#### Execute /global/conda/envs/PairedEndVariantCalling/bin/gatk --java-options "-Xms50g -Xmx50g" GenotypeGVCFs -V /global/bio/projets/GAMeR/Nicolas-Radomski/PairedEndVariant/VariantCalling/7_alignment/combined.g.vcf.gz -R /global/bio/projets/GAMeR/Nicolas-Radomski/PairedEndVariant/VariantCalling/1_reference/Enteritidis_P125109.fasta -O /global/bio/projets/GAMeR/Nicolas-Radomski/PairedEndVariant/VariantCalling/7_alignment/joint.vcf -G AS_StandardAnnotation -G StandardHCAnnotation -stand-call-conf 30 -ploidy 1
#### Execute /global/conda/envs/PairedEndVariantCalling/bin/gatk --java-options "-Xms50g -Xmx50g" SelectVariants -V /global/bio/projets/GAMeR/Nicolas-Radomski/PairedEndVariant/VariantCalling/7_alignment/joint.vcf -select-type SNP  -O /global/bio/projets/GAMeR/Nicolas-Radomski/PairedEndVariant/VariantCalling/7_alignment/joint.snps.vcf
#### Execute /global/conda/envs/PairedEndVariantCalling/bin/gatk --java-options "-Xms50g -Xmx50g" SelectVariants -V /global/bio/projets/GAMeR/Nicolas-Radomski/PairedEndVariant/VariantCalling/7_alignment/joint.vcf -select-type INDEL  -O /global/bio/projets/GAMeR/Nicolas-Radomski/PairedEndVariant/VariantCalling/7_alignment/joint.indels.vcf
#### Execute /global/conda/envs/PairedEndVariantCalling/bin/gatk --java-options "-Xms50g -Xmx50g" VariantFiltration -V /global/bio/projets/GAMeR/Nicolas-Radomski/PairedEndVariant/VariantCalling/7_alignment/joint.snps.vcf -filter "QD < 2.0" --filter-name "QD2" -filter "QUAL < 30.0" --filter-name "QUAL30" -filter "SOR > 3.0" --filter-name "SOR3" -filter "FS > 60.0" --filter-name "FS60" -filter "MQ < 40.0" --filter-name "MQ40" -filter "MQRankSum < -12.5" --filter-name "MQRankSum-12.5" -filter "ReadPosRankSum < -8.0" --filter-name "ReadPosRankSum-8"  -O /global/bio/projets/GAMeR/Nicolas-Radomski/PairedEndVariant/VariantCalling/7_alignment/filtered.snps.vcf
#### Execute /global/conda/envs/PairedEndVariantCalling/bin/gatk --java-options "-Xms50g -Xmx50g" VariantFiltration -V /global/bio/projets/GAMeR/Nicolas-Radomski/PairedEndVariant/VariantCalling/7_alignment/joint.indels.vcf -filter "QD < 2.0" --filter-name "QD2" -filter "QUAL < 30.0" --filter-name "QUAL30" -filter "SOR > 3.0" --filter-name "SOR3" -filter "FS > 60.0" --filter-name "FS60" -filter "MQ < 40.0" --filter-name "MQ40" -filter "MQRankSum < -12.5" --filter-name "MQRankSum-12.5" -filter "ReadPosRankSum < -8.0" --filter-name "ReadPosRankSum-8"  -O /global/bio/projets/GAMeR/Nicolas-Radomski/PairedEndVariant/VariantCalling/7_alignment/filtered.indels.vcf
#### Execute /global/conda/envs/PairedEndVariantCalling/bin/gatk --java-options "-Xms50g -Xmx50g" MergeVcfs -I /global/bio/projets/GAMeR/Nicolas-Radomski/PairedEndVariant/VariantCalling/7_alignment/filtered.snps.vcf -I /global/bio/projets/GAMeR/Nicolas-Radomski/PairedEndVariant/VariantCalling/7_alignment/filtered.indels.vcf -O /global/bio/projets/GAMeR/Nicolas-Radomski/PairedEndVariant/VariantCalling/7_alignment/filtered.snps.indels.vcf

'''
#### exemple of Bash command (bash_PairedEndVariantConda.sh) ####
#!/bin/bash
#SBATCH -p Research
#SBATCH -o %x.%N.%j.out
#SBATCH -e %x.%N.%j.err
#SBATCH --cpus-per-task=1
#SBATCH --job-name=test-20201012
source /global/conda/bin/activate;conda activate PairedEndVariantCalling; \
python /global/bio/projets/GAMeR/Nicolas-Radomski/PairedEndVariant/VCFtoPseudoGenome.py \
	-i /global/bio/projets/GAMeR/Nicolas-Radomski/PairedEndVariant/VariantCalling/7_alignment/filtered.snps.indels.vcf \
	-ref /global/bio/projets/GAMeR/Nicolas-Radomski/PairedEndVariant/VariantCalling/1_reference/Enteritidis_P125109.fasta \
	-o /global/bio/projets/GAMeR/Nicolas-Radomski/PairedEndVariant/VariantCalling/8_matrix/test \
	--NoINDELs

#### exemple of Bash command execution ####
sbatch bash_VariantAlignmentConda.sh
'''

import os, sys
import argparse
import genomic

# parse arguments
def get_parser():
	
	# function asking arguments
	parser = argparse.ArgumentParser(description="perform consolidation of g.vcf.gz files (CombineGVCFs) from PairedEndVariant.py, joint-calliing (GenotypeGVCFs), hard filtering of SNPs and InDels (SelectVariants and VariantFiltration) and merging of SNPs and InDels (MergeVcfs) based on GATK4 for downstream phylogenomic analyses")

	# setting of arguments

	parser.add_argument('-r', action="store", dest='run',
					type=str, required=True, 
					help='name of the run from PairedEndVariant.py (REQUIRED)')

	parser.add_argument('-gvcf', action="store", dest='gvcf',
					type=str, required=True, 
					help='path to directory of g.vcf.gz files from PairedEndVariant.py (REQUIRED)')

	parser.add_argument('-ind', action="store", dest='index',
					type=str, required=True, 
					help='path to the reference fasta file indexed by PairedEndVariant.py (REQUIRED)')

	parser.add_argument('-call', action="store", dest='gatk',
					type=str, required=True, 
					help='path to GATK4 (REQUIRED)')

	return parser

# ask run, g.vcf.gz paths, indexed reference path, GATK4 path, then return a directory 7_alignment

def main():
	
	# get parser object
	parser=get_parser()

	# print parser.help if there are no arguments in the command
	if len(sys.argv)==1:
		parser.print_help()
		sys.exit(1)

	# extract arguments from parser
	Arguments=parser.parse_args()

	# define variables of the arguments	
	r=Arguments.run
	GV=Arguments.gvcf
	IN=Arguments.index
	GA=Arguments.gatk

	# get and print working directory (wd)
	wd = os.getcwd()
	print ("#### The current working directory is %s" % wd)

	# create an output directory if they do not exist with the function nodir_makedir_error_exit of the module genomic.py or exit with a error message if it exists
	genomic.nodir_makedir_error(directory = r + '/' + '7_alignment')

	# prepare path of output directory
	alignmentoutput = wd + '/' + r + '/' + '7_alignment' + '/'

	# extract g.vcf.gz paths and output in a .txt file
	cmdgvcfpathsoutput = alignmentoutput + 'gvcfpaths.txt'
	cmdgvcfpaths = 'ls ' + GV + '''/*.g.vcf.gz | tr '\n' '%' | sed 's@.$@@' | sed 's@%@ -V @'g > ''' + cmdgvcfpathsoutput
	os.system(cmdgvcfpaths)
	print("#### Execute %s" %cmdgvcfpaths)

	# check the absence of the gvcfpaths.txt file, then return an error message exiting or a successfull message with the function absentefile_error_success of the module genomics.py
	genomic.absentefile_error_success(expectedfile = r + '/' + '7_alignment' + '/' + 'gvcfpaths.txt')

	# read cmdgvcfpaths file and keep it in variable
	gvcfpathsfile = open(cmdgvcfpathsoutput, "r")
	gvcfpathsfilecontent = gvcfpathsfile.read()
	print("#### the content of the gvcfpathsfile is %s" %gvcfpathsfilecontent)

	# prepare and run CombineGVCFs
	CombineGVCFsoutput = alignmentoutput + 'combined.g.vcf.gz'
	cmdCombineGVCFs = GA + ' --java-options "-Xms50g -Xmx50g" CombineGVCFs -R ' + IN + ' -V ' + gvcfpathsfilecontent + ' -O ' + CombineGVCFsoutput + ' -G AS_StandardAnnotation -G StandardHCAnnotation'
	os.system(cmdCombineGVCFs)
	print("#### Execute %s" %cmdCombineGVCFs)

	# close the gvcfpathsfile to allow accessibility
	gvcfpathsfile.close()

	# check the absence of the combined.g.vcf.gz file, then return an error message exiting or a successfull message with the function absentefile_error_success of the module genomics.py
	genomic.absentefile_error_success(expectedfile = r + '/' + '7_alignment' + '/' + 'combined.g.vcf.gz')

	# prepare and run GenotypeGVCFs
	GenotypeGVCFsoutput = alignmentoutput + 'joint.vcf'
	cmdGenotypeGVCFs = GA + ' --java-options "-Xms50g -Xmx50g" GenotypeGVCFs -V ' + CombineGVCFsoutput + ' -R ' + IN + ' -O ' + GenotypeGVCFsoutput + ' -G AS_StandardAnnotation -G StandardHCAnnotation -stand-call-conf 30 -ploidy 1'
	os.system(cmdGenotypeGVCFs)
	print("#### Execute %s" %cmdGenotypeGVCFs)

	# check the absence of the joint.vcf file, then return an error message exiting or a successfull message with the function absentefile_error_success of the module genomics.py
	genomic.absentefile_error_success(expectedfile = r + '/' + '7_alignment' + '/' + 'joint.vcf')

	# prepare and run SelectVariants for SNPs
	SelectSNPoutput = alignmentoutput + 'joint.snps.vcf'
	cmdSelectSNP = GA + ' --java-options "-Xms50g -Xmx50g" SelectVariants -V ' + GenotypeGVCFsoutput + ' -select-type SNP ' + ' -O ' + SelectSNPoutput
	os.system(cmdSelectSNP)
	print("#### Execute %s" %cmdSelectSNP)

	# check the absence of the joint.snps.vcf file, then return an error message exiting or a successfull message with the function absentefile_error_success of the module genomics.py
	genomic.absentefile_error_success(expectedfile = r + '/' + '7_alignment' + '/' + 'joint.snps.vcf')

	# prepare and run SelectVariants for InDels
	SelectINDELoutput = alignmentoutput + 'joint.indels.vcf'
	cmdSelectINDEL = GA + ' --java-options "-Xms50g -Xmx50g" SelectVariants -V ' + GenotypeGVCFsoutput + ' -select-type INDEL ' + ' -O ' + SelectINDELoutput
	os.system(cmdSelectINDEL)
	print("#### Execute %s" %cmdSelectINDEL)

	# check the absence of the joint.indels.vcf, then return an error message exiting or a successfull message with the function absentefile_error_success of the module genomics.py
	genomic.absentefile_error_success(expectedfile = r + '/' + '7_alignment' + '/' + 'joint.indels.vcf')

	# prepare and run VariantFiltration for SNPs
	FiltrationSNPoutput = alignmentoutput + 'filtered.snps.vcf'
	cmdFiltrationSNP = GA + ' --java-options "-Xms50g -Xmx50g" VariantFiltration -V ' + SelectSNPoutput + ' -filter "QD < 2.0" --filter-name "QD2" -filter "QUAL < 30.0" --filter-name "QUAL30" -filter "SOR > 3.0" --filter-name "SOR3" -filter "FS > 60.0" --filter-name "FS60" -filter "MQ < 40.0" --filter-name "MQ40" -filter "MQRankSum < -12.5" --filter-name "MQRankSum-12.5" -filter "ReadPosRankSum < -8.0" --filter-name "ReadPosRankSum-8" ' + ' -O ' + FiltrationSNPoutput
	os.system(cmdFiltrationSNP)
	print("#### Execute %s" %cmdFiltrationSNP)

	# check the absence of the filtered.snps.vcf, then return an error message exiting or a successfull message with the function absentefile_error_success of the module genomics.py
	genomic.absentefile_error_success(expectedfile = r + '/' + '7_alignment' + '/' + 'filtered.snps.vcf')

	# prepare and run VariantFiltration for InDels
	FiltrationINDELoutput = alignmentoutput + 'filtered.indels.vcf'
	cmdFiltrationINDEL = GA + ' --java-options "-Xms50g -Xmx50g" VariantFiltration -V ' + SelectINDELoutput + ' -filter "QD < 2.0" --filter-name "QD2" -filter "QUAL < 30.0" --filter-name "QUAL30" -filter "SOR > 3.0" --filter-name "SOR3" -filter "FS > 60.0" --filter-name "FS60" -filter "MQ < 40.0" --filter-name "MQ40" -filter "MQRankSum < -12.5" --filter-name "MQRankSum-12.5" -filter "ReadPosRankSum < -8.0" --filter-name "ReadPosRankSum-8" ' + ' -O ' + FiltrationINDELoutput
	os.system(cmdFiltrationINDEL)
	print("#### Execute %s" %cmdFiltrationINDEL)

	# check the absence of the filtered.indels.vcf, then return an error message exiting or a successfull message with the function absentefile_error_success of the module genomics.py
	genomic.absentefile_error_success(expectedfile = r + '/' + '7_alignment' + '/' + 'filtered.indels.vcf')

	# prepare and run MergeVcfs (solves overlapping)
	MergeVcfsoutput = alignmentoutput + 'filtered.snps.indels.vcf'
	cmdMergeVcfs = GA + ' --java-options "-Xms50g -Xmx50g" MergeVcfs -I ' + FiltrationSNPoutput + ' -I ' + FiltrationINDELoutput + ' -O ' + MergeVcfsoutput
	os.system(cmdMergeVcfs)
	print("#### Execute %s" %cmdMergeVcfs)

	# check the absence of the filtered.snps.indels.vcf, then return an error message exiting or a successfull message with the function absentefile_error_success of the module genomics.py
	genomic.absentefile_error_success(expectedfile = r + '/' + '7_alignment' + '/' + 'filtered.snps.indels.vcf')

	# congtratulate users with the function congratulation of the module genomic.py
	genomic.congratulation()

# driver code: if the code above is a scrypt, call  main() function, rather than to considere it as a module
if __name__ == "__main__":
	# calling main() function
	main()
