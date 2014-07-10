Geordi data lifecycle/terminology
=================================

1. Importing: This is the process of putting data into geordi. It's done with manager commands, either directly with the 'add data item' command, with an 'add folder' command, or with purpose-built importers, which reside in the geordi/data/importer/ directory. Updating data is simply re-importing it, which should preserve matches and other such information.

2. Matching: After importing, items that are already in MusicBrainz may be marked as such by way of matching. Initially, this will only be with 'raw' matches, i.e., those stored within geordi. In the future, it should also be possible for matches to be derived from URL relationships and other properties of the MusicBrainz database, presumably upon replication.

3. Seeding: Geordi's mapped data can be converted into a format that allows adding it to MusicBrainz. Eventually, it should also be possible for the same process to provide suggested edits, and seed pages that edit data, rather than those that add information exclusively, but this will probably depend on having replicated data from MusicBrainz.

4. Merging and Splitting: not yet implemented, but it will eventually be possible to link two items, by way of an interface to specify their connection (potentially via intermediate objects such as release groups, areas, etc.). Likewise, it should be possible to split items by assigning their data items, links, and matches to two sides.