class Program:
    def Main(self, *args):
        command = args[0]
        
        match command:
            case "generate2":
                seed = ""
                if len(args) > 3:
                    seed = args[4]
                #TODO: Create Randomizer.CreateInputJson method
            case "generate_final_output2":
                #TODO: Create Randomizer.GenerateFinalOutput2 method
                pass
            case "print_check_ids":
                #TODO: Create Logic/CheckIds/CheckIdsClass
                pass
            case "print_seed_gen_results":
                #TODO Create Randomizer.GetSeedGenResultsJson method
                pass
            case _:
                raise Exception("Unrecognized command.")