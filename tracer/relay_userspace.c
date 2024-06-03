#include <stdio.h>
#include "librelay.h"

/* relayfs base file name */
static char *kleak_filebase = "/mnt/relay/kleak/cpu";

/* logging output written here, filebase0...N */
static char *kleak_outfilebase = "kleak";

/* internal variables */
#define DEFAULT_SUBBUF_SIZE (262144)
#define DEFAULT_N_SUBBUFS (4)
static unsigned subbuf_size = DEFAULT_SUBBUF_SIZE;
static unsigned n_subbufs = DEFAULT_N_SUBBUFS;

static void usage(void)
{
	fprintf(stderr, "kleak [-b subbuf_size -n n_subbufs]\n");
	exit(1);
}

int main(int argc, char **argv)
{
	extern char *optarg;
	extern int optopt;
	int c;
	unsigned opt_subbuf_size = 0;
	unsigned opt_n_subbufs = 0;

	while ((c = getopt(argc, argv, "b:n:")) != -1) {
		switch (c) {
		case 'b':
			opt_subbuf_size = (unsigned)atoi(optarg);
			if (!opt_subbuf_size)
				usage();
			break;
		case 'n':
			opt_n_subbufs = (unsigned)atoi(optarg);
			if (!opt_n_subbufs)
				usage();
			break;
		case '?':
			printf("Unknown option -%c\n", optopt);
			usage();
			break;
		default:
			break;
		}
	}

	if ((opt_n_subbufs && !opt_subbuf_size) ||
	    (!opt_n_subbufs && opt_subbuf_size))
		usage();
	
	if (opt_n_subbufs && opt_n_subbufs) {
		subbuf_size = opt_subbuf_size;
		n_subbufs = opt_n_subbufs;
	}

	/* use _init... function because we want a different netlink 'unit' */

	if (init_relay_app(kleak_filebase, kleak_outfilebase,
			   subbuf_size, n_subbufs, 1)) {
		printf("Couldn't initialize relay app. Exiting.\n");
		exit(1);
	}

	printf("Creating channel with %u sub-buffers of size %u.\n",
	       n_subbufs, subbuf_size);
	printf("Logging... Press Control-C to stop.\n");

	/* use _init... function because we want a different netlink 'unit' */
	if (relay_app_main_loop()) {
		printf("Couldn't enter main loop. Exiting.\n");
		exit(1);
	}
}