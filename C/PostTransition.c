#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX_STRING_LENGTH 6

struct package
{
	char* id;
	int weight;
};

typedef struct package package;

struct post_office
{
	int min_weight;
	int max_weight;
	package* packages;
	int packages_count;
};

typedef struct post_office post_office;

struct town
{
	char* name;
	post_office* offices;
	int offices_count;
};

typedef struct town town;

void print_all_packages(town t) {

    printf("%s:\n", t.name);
    
    for (int o=0; o<t.offices_count; o++) {
        printf("\t%d:\n", o);
        for (int p=0; p<t.offices[o].packages_count; p++){
            printf("\t\t%s\n", t.offices[o].packages[p].id);
        }
    }
}

int total_packages(town t){

    int total = 0;

    for (int i=0; i<t.offices_count; i++){
        total += t.offices[i].packages_count;
    }

    return total;

}

int total_packages(town t);

int isAcceptable(package p, post_office office) {

    if (p.weight <= office.max_weight && p.weight >= office.min_weight)
        return 1;

    return 0;

}

void send_all_acceptable_packages(town* source, int source_office_index, town* target, int target_office_index) {	

    int p = 0;
    while (p < source->offices[source_office_index].packages_count) {

        if (isAcceptable(source->offices[source_office_index].packages[p], target->offices[target_office_index])) {
            // target office receiving package
            
            target->offices[target_office_index].packages = realloc(target->offices[target_office_index].packages, (target->offices[target_office_index].packages_count + 1) * sizeof(package));

            target->offices[target_office_index].packages[target->offices[target_office_index].packages_count++] = source->offices[source_office_index].packages[p];
            
            // source office deleting sent package

            for (int i=p; i<source->offices[source_office_index].packages_count - 1; i++)
                source->offices[source_office_index].packages[i] = source->offices[source_office_index].packages[i+1];

            source->offices[source_office_index].packages = realloc(source->offices[source_office_index].packages, (source->offices[source_office_index].packages_count - 1) * sizeof(package));
            source->offices[source_office_index].packages_count--;

            continue;
        }

        p++;

    }

}

town town_with_most_packages(town* towns, int towns_count) {

    town richest;
    int most = 0;

    for (int i=0; i<towns_count; i++){
        if (total_packages(towns[i]) > most){
            most = total_packages(towns[i]);
            richest = towns[i];
        }

    }

    return richest;
}

town* find_town(town* towns, int towns_count, char* name) {

    town* found = NULL;

    for (int i=0; i<towns_count; i++){
        if (strcmp(towns[i].name, name) == 0)
            found = &towns[i];
    }

    return found;
}

int main()
{
	int towns_count;
	scanf("%d", &towns_count);
	town* towns = malloc(sizeof(town)*towns_count);
	for (int i = 0; i < towns_count; i++) {
		towns[i].name = malloc(sizeof(char) * MAX_STRING_LENGTH);
		scanf("%s", towns[i].name);
		scanf("%d", &towns[i].offices_count);
		towns[i].offices = malloc(sizeof(post_office)*towns[i].offices_count);
		for (int j = 0; j < towns[i].offices_count; j++) {
			scanf("%d%d%d", &towns[i].offices[j].packages_count, &towns[i].offices[j].min_weight, &towns[i].offices[j].max_weight);
			towns[i].offices[j].packages = malloc(sizeof(package)*towns[i].offices[j].packages_count);
			for (int k = 0; k < towns[i].offices[j].packages_count; k++) {
				towns[i].offices[j].packages[k].id = malloc(sizeof(char) * MAX_STRING_LENGTH);
				scanf("%s", towns[i].offices[j].packages[k].id);
				scanf("%d", &towns[i].offices[j].packages[k].weight);
			}
		}
	}
	int queries;
	scanf("%d", &queries);
	char town_name[MAX_STRING_LENGTH];
	while (queries--) {
		int type;
		scanf("%d", &type);
		switch (type) {
		case 1:
			scanf("%s", town_name);
			town* t = find_town(towns, towns_count, town_name);
			print_all_packages(*t);
			break;
		case 2:
			scanf("%s", town_name);
			town* source = find_town(towns, towns_count, town_name);
			int source_index;
			scanf("%d", &source_index);
			scanf("%s", town_name);
			town* target = find_town(towns, towns_count, town_name);
			int target_index;
			scanf("%d", &target_index);
			send_all_acceptable_packages(source, source_index, target, target_index);
			break;
		case 3:
			printf("Town with the most number of packages is %s\n", town_with_most_packages(towns, towns_count).name);
			break;
		}
	}
	return 0;
}
