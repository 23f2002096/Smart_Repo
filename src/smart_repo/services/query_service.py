from smart_repo.services.repository_store import RepositoryStore


class QueryService:
    """
    Query the parsed repository.
    """

    def __init__(self):
        self.repository = RepositoryStore.get()

    def get_all_files(self):
        if self.repository is None:
            return []

        return self.repository.files

    def find_file(self, filename: str):

        if self.repository is None:
            return None

        for parsed_file in self.repository.files:

            if parsed_file.file.name == filename:
                return parsed_file

        return None

    def find_function(self, function_name: str):

        if self.repository is None:
            return []

        results = []

        for parsed_file in self.repository.files:

            for function in parsed_file.functions:

                if function.name == function_name:

                    results.append(
                        {
                            "file": parsed_file.file.relative_path,
                            "function": function,
                        }
                    )

        return results

    def find_class(self, class_name: str):

        if self.repository is None:
            return []

        results = []

        for parsed_file in self.repository.files:

            for cls in parsed_file.classes:

                if cls.name == class_name:

                    results.append(
                        {
                            "file": parsed_file.file.relative_path,
                            "class": cls,
                        }
                    )

        return results

    def find_import(self, module_name: str):

        if self.repository is None:
            return []

        results = []

        for parsed_file in self.repository.files:

            for imp in parsed_file.imports:

                if module_name.lower() in imp.module.lower():

                    results.append(
                        {
                            "file": parsed_file.file.relative_path,
                            "module": imp.module,
                        }
                    )

        return results