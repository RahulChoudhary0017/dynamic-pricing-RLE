Dynamic Pricing Reinforcement Learning Architecture

                +------------------------+
                |     Environment        |
                |------------------------|
                | Inventory              |
                | Days Left              |
                | Competitor Price       |
                +-----------+------------+
                            |
                            v
                     Current State
                            |
                            v
                +------------------------+
                |    Q-Learning Agent    |
                |------------------------|
                | Select Pricing Action  |
                +-----------+------------+
                            |
                            v
                +------------------------+
                | Customer Demand Model  |
                +-----------+------------+
                            |
                            v
                Revenue & Reward
                            |
                            v
                Update Q-Table
                            |
                            v
                   Next Episode